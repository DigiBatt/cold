
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .PicoPrefixedUnitModule import PicoPrefixedUnit



from .DensityUnitModule import DensityUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit





from .GramPerMilliLitreModule import GramPerMilliLitre






class PicoGramPerMilliLitre(PicoPrefixedUnit, DensityUnit, SINonCoherentUnit, PrefixedUnit):
    """
    Class representing the `PicoGramPerMilliLitre` entity, which inherits from:
    - PicoPrefixedUnit, DensityUnit, SINonCoherentUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#PicoGramPerMilliLitre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PicoGramPerMilliLitre'`
        - **Alias**: `class_name`
    
    - `hasUnitNonPrefixPart` (`Optional[GramPerMilliLitre]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitNonPrefixPart`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
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
    obj = PicoGramPerMilliLitre(
    
    class_iri='https://w3id.org/emmo#PicoGramPerMilliLitre',
    
    class_name='PicoGramPerMilliLitre',
    
    hasUnitNonPrefixPart="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    elucidation="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#PicoGramPerMilliLitre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PicoGramPerMilliLitre',
        
        alias="class_name"
    )
    
    hasUnitNonPrefixPart: Optional[GramPerMilliLitre] = Field(
        
            None,
        
        alias="hasUnitNonPrefixPart"
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
    


    
    @validator("hasUnitNonPrefixPart", pre=True, always=True)
    def validate_hasUnitNonPrefixPart(cls, value):
        if value is not None and not isinstance(value, GramPerMilliLitre):
            raise ValueError(f"Field 'hasUnitNonPrefixPart' must be an instance of 'GramPerMilliLitre' or its subclass.")
        return value
    
    

    

    