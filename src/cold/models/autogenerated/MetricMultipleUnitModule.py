
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel








class MetricMultipleUnit(LinkedDataModel):
    """
    Class representing the `MetricMultipleUnit` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2024fca1_b015_45ee_9490_e9e7d36bf704'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetricMultipleUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetricMultipleUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_2024fca1_b015_45ee_9490_e9e7d36bf704',
    
    class_name='MetricMultipleUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_2024fca1_b015_45ee_9490_e9e7d36bf704',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MetricMultipleUnit',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    