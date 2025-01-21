
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .FemtoPrefixedUnitModule import FemtoPrefixedUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .AmountConcentrationUnitModule import AmountConcentrationUnit





from .MolePerLitreModule import MolePerLitre






class FemtoMolePerLitre(FemtoPrefixedUnit, SINonCoherentUnit, PrefixedUnit, AmountConcentrationUnit):
    """
    Class representing the `FemtoMolePerLitre` entity, which inherits from:
    - FemtoPrefixedUnit, SINonCoherentUnit, PrefixedUnit, AmountConcentrationUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#FemtoMolePerLitre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FemtoMolePerLitre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasUnitSymbol` (`Optional[MolePerLitre]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FemtoMolePerLitre(
    
    class_iri='https://w3id.org/emmo#FemtoMolePerLitre',
    
    class_name='FemtoMolePerLitre',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    hasUnitSymbol="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#FemtoMolePerLitre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'FemtoMolePerLitre',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasUnitSymbol: Optional[MolePerLitre] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    


    
    @validator("hasUnitSymbol", pre=True, always=True)
    def validate_hasUnitSymbol(cls, value):
        if value is not None and not isinstance(value, MolePerLitre):
            raise ValueError(f"Field 'hasUnitSymbol' must be an instance of 'MolePerLitre' or its subclass.")
        return value
    
    

    

    