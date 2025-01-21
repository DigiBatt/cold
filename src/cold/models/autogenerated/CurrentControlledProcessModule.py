
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalMeasurementProcessModule import ElectrochemicalMeasurementProcess







class CurrentControlledProcess(ElectrochemicalMeasurementProcess):
    """
    Class representing the `CurrentControlledProcess` entity, which inherits from:
    - ElectrochemicalMeasurementProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5548f188_df00_4c05_ae98_7846e92efe36'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentControlledProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentControlledProcess(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5548f188_df00_4c05_ae98_7846e92efe36',
    
    class_name='CurrentControlledProcess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5548f188_df00_4c05_ae98_7846e92efe36',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentControlledProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    