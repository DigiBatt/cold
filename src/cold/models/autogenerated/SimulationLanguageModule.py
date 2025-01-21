
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ModellingLanguageModule import ModellingLanguage



from .DescriptionModule import Description



from .InformationModule import Information







class SimulationLanguage(ModellingLanguage, Description, Information):
    """
    Class representing the `SimulationLanguage` entity, which inherits from:
    - ModellingLanguage, Description, Information

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_03d4cd70_0d16_4403_b68c_d41a9117f981'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SimulationLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SimulationLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_03d4cd70_0d16_4403_b68c_d41a9117f981',
    
    class_name='SimulationLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_03d4cd70_0d16_4403_b68c_d41a9117f981',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SimulationLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    