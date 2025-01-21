
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel








class MetricSubMultipleUnit(LinkedDataModel):
    """
    Class representing the `MetricSubMultipleUnit` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9d28f9ad_d9d3_4edb_bc00_5d9bd242244d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetricSubMultipleUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetricSubMultipleUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_9d28f9ad_d9d3_4edb_bc00_5d9bd242244d',
    
    class_name='MetricSubMultipleUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_9d28f9ad_d9d3_4edb_bc00_5d9bd242244d',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MetricSubMultipleUnit',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    