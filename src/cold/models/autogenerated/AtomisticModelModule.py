
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialsModelModule import MaterialsModel







class AtomisticModel(MaterialsModel):
    """
    Class representing the `AtomisticModel` entity, which inherits from:
    - MaterialsModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomisticModel'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomisticModel(
    
    class_iri='https://w3id.org/emmo#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213',
    
    class_name='AtomisticModel',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_84cadc45_6758_46f2_ba2a_5ead65c70213',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomisticModel',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    