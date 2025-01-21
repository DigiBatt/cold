
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPropertyModule import ElectrochemicalProperty







class Polarity(ElectrochemicalProperty):
    """
    Class representing the `Polarity` entity, which inherits from:
    - ElectrochemicalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_16a5de33_a2ca_4563_80d4_6caeb08d97ca'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Polarity'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Polarity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_16a5de33_a2ca_4563_80d4_6caeb08d97ca',
    
    class_name='Polarity',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_16a5de33_a2ca_4563_80d4_6caeb08d97ca',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Polarity',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    