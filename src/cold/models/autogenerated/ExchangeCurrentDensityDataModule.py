
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class ExchangeCurrentDensityData(DataSet):
    """
    Class representing the `ExchangeCurrentDensityData` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7ea60b2_18f4_4588_bf19_55539c8e8888'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ExchangeCurrentDensityData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ExchangeCurrentDensityData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7ea60b2_18f4_4588_bf19_55539c8e8888',
    
    class_name='ExchangeCurrentDensityData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7ea60b2_18f4_4588_bf19_55539c8e8888',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ExchangeCurrentDensityData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    