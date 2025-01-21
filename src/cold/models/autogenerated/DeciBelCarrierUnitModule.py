
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .DeciPrefixedUnitModule import DeciPrefixedUnit



from .NonSIUnitModule import NonSIUnit



from .LogarithmicUnitModule import LogarithmicUnit



from .PrefixedUnitModule import PrefixedUnit








class DeciBelCarrierUnit(DeciPrefixedUnit, NonSIUnit, LogarithmicUnit, PrefixedUnit):
    """
    Class representing the `DeciBelCarrierUnit` entity, which inherits from:
    - DeciPrefixedUnit, NonSIUnit, LogarithmicUnit, PrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#DeciBelCarrierUnit'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeciBelCarrierUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `unitSymbol` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `unitSymbol`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DeciBelCarrierUnit(
    
    class_iri='https://w3id.org/emmo#DeciBelCarrierUnit',
    
    class_name='DeciBelCarrierUnit',
    
    elucidation="example_value",
    
    qudtReference="example_value",
    
    unitSymbol="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#DeciBelCarrierUnit',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'DeciBelCarrierUnit',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    unitSymbol: Optional[str] = Field(
        
            None,
        
        alias="unitSymbol"
    )
    


    
    

    

    