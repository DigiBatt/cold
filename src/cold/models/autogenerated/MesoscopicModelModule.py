
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialsModelModule import MaterialsModel







class MesoscopicModel(MaterialsModel):
    """
    Class representing the `MesoscopicModel` entity, which inherits from:
    - MaterialsModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_53935db0_af45_4426_b9e9_244a0d77db00'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MesoscopicModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MesoscopicModel(
    
    class_iri='https://w3id.org/emmo#EMMO_53935db0_af45_4426_b9e9_244a0d77db00',
    
    class_name='MesoscopicModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_53935db0_af45_4426_b9e9_244a0d77db00',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MesoscopicModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    