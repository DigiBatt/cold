
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DensityUnitModule import DensityUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .NanoPrefixedUnitModule import NanoPrefixedUnit








class NanoGramPerMicroLitre(DensityUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit):
    """
    Class representing the `NanoGramPerMicroLitre` entity, which inherits from:
    - DensityUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NanoGramPerMicroLitre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoGramPerMicroLitre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
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
    obj = NanoGramPerMicroLitre(
    
    class_iri='https://w3id.org/emmo#NanoGramPerMicroLitre',
    
    class_name='NanoGramPerMicroLitre',
    
    hasSIConversionMultiplier="example_value",
    
    ucumCode="example_value",
    
    unitSymbol="example_value",
    
    qudtReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NanoGramPerMicroLitre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NanoGramPerMicroLitre',
        
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
    


    
    

    

    