
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialsModelModule import MaterialsModel







class ContinuumModel(MaterialsModel):
    """
    Class representing the `ContinuumModel` entity, which inherits from:
    - MaterialsModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ContinuumModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ContinuumModel(
    
    class_iri='https://w3id.org/emmo#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea',
    
    class_name='ContinuumModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4456a5d2_16a6_4ee1_9a8e_5c75956b28ea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ContinuumModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    