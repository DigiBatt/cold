
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .MassUnitModule import MassUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .PrefixedUnitModule import PrefixedUnit



from .NanoPrefixedUnitModule import NanoPrefixedUnit








class NanoGram(MassUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit):
    """
    Class representing the `NanoGram` entity, which inherits from:
    - MassUnit, SINonCoherentUnit, PrefixedUnit, NanoPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#NanoGram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NanoGram'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `hasUnitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasUnitSymbol`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NanoGram(
    
    class_iri='https://w3id.org/emmo#NanoGram',
    
    class_name='NanoGram',
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    hasUnitSymbol="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#NanoGram',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'NanoGram',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    hasUnitSymbol: Optional[str] = Field(
        
            None,
        
        alias="hasUnitSymbol"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    